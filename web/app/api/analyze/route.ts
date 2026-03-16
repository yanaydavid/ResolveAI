import { NextRequest, NextResponse } from "next/server";
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const {
      caseTitle,
      partyOneName,
      partyOneEmail,
      partyTwoName,
      partyTwoEmail,
      category,
      description,
      lang = "he",
    } = body;

    if (!caseTitle || !partyOneName || !partyTwoName || !description) {
      return NextResponse.json(
        { error: "Missing required fields" },
        { status: 400 }
      );
    }

    const outputLang = lang === "he" ? "Hebrew" : "English";
    const caseId = `RA-${Date.now().toString().slice(-8)}`;

    const prompt = `You are a senior AI arbitrator with expertise in commercial law, contract disputes, employment law, real estate law, and financial disputes. You approach every case with strict impartiality, basing your analysis exclusively on the facts and arguments presented. Your decisions are thorough, reasoned, and professionally written.

Analyze the following arbitration case and render a decision.

CASE DETAILS:
- Case ID: ${caseId}
- Title: ${caseTitle}
- Category: ${category}
- Claimant (Party 1): ${partyOneName} (${partyOneEmail})
- Respondent (Party 2): ${partyTwoName} (${partyTwoEmail})
- Dispute Description:
${description}

INSTRUCTIONS:
1. Carefully analyze both the explicit claims and the legal principles applicable to this category of dispute.
2. Consider both parties' likely positions based on the description provided.
3. Apply relevant legal frameworks and principles of fairness.
4. Render a clear, definitive finding.
5. Provide comprehensive legal reasoning.
6. Write ALL response text in ${outputLang}.

CRITICAL: Respond ONLY with a valid JSON object — no markdown fences, no text before or after the JSON. The structure must be exactly:
{
  "caseId": "${caseId}",
  "caseTitle": "${caseTitle}",
  "partyOneName": "${partyOneName}",
  "partyTwoName": "${partyTwoName}",
  "category": "${category}",
  "lang": "${lang}",
  "summary": "A concise 2-3 sentence neutral summary of the dispute as presented. Write in ${outputLang}.",
  "analysis": "Thorough analysis in 3-4 substantial paragraphs examining: (a) the factual background, (b) the applicable legal principles, (c) the merits of each party's position, and (d) any mitigating or aggravating factors. Write in ${outputLang}.",
  "finding": "Your clear, definitive arbitration finding — state which party prevails and on what basis, or indicate a split finding if warranted. 2-3 sentences. Write in ${outputLang}.",
  "rationale": "The legal and factual reasoning supporting your finding, in 2-3 paragraphs. Cite the specific principles and evidence points that drove your conclusion. Write in ${outputLang}.",
  "nextSteps": [
    "First concrete, actionable step for the parties",
    "Second concrete step",
    "Third concrete step",
    "Fourth step if applicable"
  ]
}`;

    const message = await client.messages.create({
      model: "claude-sonnet-4-6",
      max_tokens: 2000,
      messages: [{ role: "user", content: prompt }],
    });

    const content = message.content[0];
    if (content.type !== "text") {
      throw new Error("Unexpected response type from Claude");
    }

    // Strip any accidental markdown fences
    const raw = content.text
      .replace(/^```json\s*/i, "")
      .replace(/^```\s*/i, "")
      .replace(/\s*```$/i, "")
      .trim();

    const verdict = JSON.parse(raw);

    return NextResponse.json(verdict);
  } catch (err) {
    console.error("Analyze API error:", err);
    return NextResponse.json(
      { error: "Failed to process arbitration request" },
      { status: 500 }
    );
  }
}
