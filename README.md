## Chosen IAE Features 
1. Vocabulary
2. Authority

## How I Translated Them Into Prompt Rules
  To capture the IAE vocabulary use described by Alix Rule & David Levine, I noted the importance of replacing adverbs with their noun counterparts. Examples in the text include: "visual becomes visuality, global becomes globality, potential becomes potentiality, experience becomes experiencability." This rule is fed into the model by writing the prompt with, "Limit the use of adverbs in the text; replace these words with their noun equivalent." Furthermore, the prompt features, "include some variation of the word reality or space in the text"; this fulfills the importance of describing the environment in abstract, self-important terms. This flowery, illogical language makes up the backbone of IAE, creating writing that isn't quite English but masquerades as highly attuned and knowledgeable, while being nonsensical. 
  To instill a sense of authority, I have instructed the model to speak with an arrogant and elitist tone. I prompted, "You are highly university-level trained, you are the authority on this subject; speak exclusively in INTERNATIONAL ART ENGLISH"

## How The Image Prompt Is Derived From The Label
When the label is generated, it stores the text output into strings for the title, artist, medium, etc. This is so that the individual information can be formatted properly in HMTL but also so that these strings can be instanced into the image generation prompt. I take a base prompt that tells the image the context of a gallery, and fill in the blank instructions to follow for the size, medium, title context.