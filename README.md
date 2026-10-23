## Chosen IAE Features 
1. Vocabulary
   - Replacing adverbs with nouns
   - Excessive use of reality/space, conflicting use of abstract and physical environment descriptors
3. Authority
   - Arrogant, elitist, highly educated tone
   
## How I Translated Them Into Prompt Rules
  To capture the IAE vocabulary use described by Alix Rule & David Levine, I noted the importance of replacing adverbs with their noun counterparts. Examples in the text include: "visual becomes visuality, global becomes globality, potential becomes potentiality, experience becomes experiencability." This rule is fed into the model by writing the prompt with, "Limit the use of adverbs in the text; replace these words with their noun equivalent." Furthermore, the prompt features, "include some variation of the word reality or space in the text"; this fulfills the importance of describing the environment in abstract, self-important terms. This flowery, illogical language makes up the backbone of IAE, creating writing that isn't quite English but masquerades as highly attuned and knowledgeable, while being nonsensical. 
  To instill a sense of authority, I have instructed the model to speak with an arrogant and elitist tone. I prompted, "You are highly university-level trained; you are the authority on this subject; speak exclusively in INTERNATIONAL ART ENGLISH"

## How The Image Prompt Is Derived From The Label
When the label is generated, it stores the text output into strings for the title, artist, medium, etc. This is so that the individual information can be formatted properly in HMTL but also so that these strings can be inserted into the image generation prompt. I take a base prompt that tells the image the context of a gallery, and fill in the blank instructions to follow for the size, medium, and title context.

## A User Guide For The Web App
  To begin, describe objects or abstract concepts in short terms in the text box. When satisfied, click the button labelled “open the exhibit" and wait for the gallery installation to be generated. Once complete, you can click the button at the top of the page saying “create another” to be brought back to the previous page where you can input a new prompt.

## Reflection - Why The LM is Fluent in This Dialect
  The model has been given personality cues that follow many of the IAE rules outlined by Alix Rule & David Levine. Since the model has no concept of generating logical text, it is not hindered by our human need to make sense. Instead, it can do what it is best at: generate the next most likely token and output text that doesn't quite make sense with what seems to be complete certainty. So much of speaking in IAE is acting as though you are the authority on the subject you write, speaking in flowery language, and including just the right buzzwords (vocabulary mentioned by the paper) in order to seem convincing. 
