import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Prep Prompt:\n\nI will provide prompts sequentially to guide you in developing performance statements. Please follow along with \neach prompt until you receive the instruction to create statements. Let me know when you are ready for the next \nprompt.\n\nPrompt 1a:\n\nWhen drafting performance statements, focus on highlighting the 1-2 Airman Leadership Qualities (ALQs) that most \nalign with the Airman's key achievements and strengths.\nThe 10 ALQs are:\nDelivering Results\nManaging Resources\nBuilding Teams and Coalitions\nAccountability\nInnovation\nStrategic Vision\nInitiative\nConfidence\nDeveloping Self and Others\nLeveraging Diversity\nLet me know when you're ready for the next prompt on Major Performance Areas.\n\nPrompt 1b:\n\nLet's outline the headings and definitions of Major Performance Areas (MPAs) to categorize accomplishments:\n**Executing the Mission:**\n\n- Job proficiency: Demonstrates knowledge and professional skill in assigned duties, achieving positive results and \nimpact in support of the mission.\n- Initiative: Assesses and takes independent or directed action to complete a task or mission that influences the \nmission or organization.\n- Adaptability: Adjusts to changing conditions, to include plans, information, processes, requirements, and \nobstacles in accomplishing the mission.\nLet me know when you're ready for more information.\n\n\nPrompt 1c:\n \nContinuing our categorization of Major Performance Areas (MPAs):\n**Leading People:**\n- Inclusion and teamwork: Collaborates effectively with others to achieve an inclusive climate in pursuit of a \ncommon goal or to complete a task or mission.\n- Emotional intelligence: Exercises self-awareness, manages their own emotions effectively; demonstrates an \nunderstanding of others' emotions, and appropriately manages relationships.\n- Communication: Articulates information in a clear and timely manner, both verbally and non-verbally, through \nactive listening and messaging tailored to the appropriate audience.\nLet me know when you're ready for more information.\n\nPrompt 1d:\n \nContinuing our categorization of Major Performance Areas (MPAs):\n**Managing Resources:**\n- Stewardship: Demonstrates responsible management of assigned resources, which may include Eme, equipment, \npeople, funds and/or facilities.\n- Accountability: Takes responsibility for the actions and behaviors of self and/or team; demonstrates reliability and \ntransparency.\nLet me know when you're ready for more information.\n\nPrompt 1e:\n\nFinal part of our categorization of Major Performance Areas (MPAs):\n**Improving the Organization:**\n- Decision Making: Makes well-informed, effective, and timely decisions under one's control that weigh constraints, \nrisks, and benefits.\n- Innovation: Thinks creatively about different ways to solve problems, implements improvements, and \ndemonstrates calculated risk-taking.\nYou now have a clear understanding of the ALQs and MPAs. Let me know when you're ready for the next prompt.\n\nPrompt 2:\n\nLet's outline the \"Exceptionally Skilled\" proficiency level that we want to highlight in statements:\nConsistently exhibits this quality in their behavior and serves as a role model\nProactively develops this quality in others across the organization\nAchieves significant organizational impact\nIs sought out by leadership for expertise\nInspires and equips others to handle responsibilities independently\nThe goal is to write statements from this perspective, demonstrating the airman performs at an \"Exceptionally \nSkilled\" level.\nWhen you're ready, we'll look at example statements\n\nPrompt 3:\n\nLet's look at some example statements demonstrating the \"Exceptionally Skilled\" proficiency level:\nExample 1:\nMichelle was selected #1 of 38 MTIs as the 331 TRS' NCOIC of Training (E-7 billet). She created the Group's 15-page \nTrainer guide & refined the MTI certifying process. She increased Group Trainers by 50% quarterly, totaling 64 \ncertified 30% faster than previous iterations, reduced workloads & delivered 1:1 trainer/student ratio...a 1st in 3 \nyears.\nThis example demonstrates the ALQ \"Delivering Results\" and aligns with the MPA \"Executing the Mission\".\nExample 2:\nJimmy restructured the unit's communications by initiating bi-weekly shared flight discussions improving the unit's \ncohesion, which was instrumental in earning a UEI \"Effective\" rating, the PACAF Inspector General Superior Team \naward, 12 Group and 3 Wing quarterlies, 4 Group annual award winners and his selection as the group's Sijan SNCO \nnominee.\nThis example demonstrates the ALQ \"Building Teams and Coalitions\" and aligns with the MPA \"Improving the Unit\".\nWe have 2 more examples to review, let me know when you're ready. \n\nPrompt 3A\nContinuing example statements demonstrating the \"Exceptionally Skilled\" proficiency level:\nExample 3:\nSMSgt McNasty led 25 Amn through 4 Multinational Large Force Exercises in the maintenance of 250 equipment \nitems. This produced the live firing of 18 AGM-88s and release of 57K lbs of muns! Additionally, as AF Ball Projo, he \nguided 12 committees executing a $25K budget and hosted 500 attendees with 186 DVs resulting in recognition of \n50 Amn!\nThis example demonstrates the ALQ \"Leading People\" and aligns with the MPA \"Improving the Unit\".\nExample 4:\nDT replaced and selectively manned positions in the unit which resolved broken quality assurance, security, \ntraining, and self inspection programs. His leadership led to the closure of 12 inspection deficiencies over 30-\nmonths old, reduced upgrade training timelines 6 months, and received zero Unit Effectiveness Inspection findings \nby PACAF IG.\nThis example demonstrates the ALQ \"Managing Resources\" and aligns with the MPA \"Improving the Unit\".\nThe 4 example statements exemplify:\nServing as a role model and developing others\nAchieving broad organizational impact\nReceiving recognition from leadership\nUse these examples to model your own statements at the \"Exceptionally Skilled\" level. Let me know when you're \nready to begin drafting\n\nPrompt 4:\n\nLet's do a collaborative drafting exercise to create an \"Exceptionally Skilled\" statement:\nI will provide a high-level accomplishment.\nRefer to the examples and guidelines.\nDraH your initial statement and share it with me.\nI will provide feedback to refine the statement.\nWe'll iterate until it aligns with the \"Exceptionally Skilled\" criteria.\nThere are rules we must follow, let me know when you're ready for them. \n\nPrompt 4a\nRules:\n350 characters max\nIdentify ALQs without stating explicitly\nUse active voice, optimize brevity\nInclude action and impact\nPlain language\nExceptionally skilled perspective\nstandalone sentence\nPast tense\nAvoid uncommon acronyms\nLet me know once you're ready to begin the exercise.\n\nPrompt 5:\n\nNow that we've completed the collaborative drafting exercise, let's validate alignment of the statements before \nfinalizing:\nDo the statements highlight the selected 1-2 ALQs that exemplify the airman's key contributions?\nAre the statements written from an \"Exceptionally Skilled\" perspective?\nDo they demonstrate broad organizational impact?\nDo they showcase development of others across the organization?\nWould leadership recognize this airman's expertise based on these statements?\nIs the language clear, concise, and optimized for brevity?\nDo the statements meet the standalone test?\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I'm ready for the next prompt!  I've carefully reviewed the information about ALQs, MPAs, and the \"Exceptionally Skilled\" proficiency level. I'm excited to start drafting performance statements. \n",
      ],
    },
  ]
)

# print(chat_session.send_message("hello world!").text)



