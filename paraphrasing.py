from googletrans import Translator

translator=Translator()

def Paraphrasing(in_text):
    phrased = []
    for i in ['ko', 'ja', 'el', 'fr', 'tl', 'ar', 'ht','af', 'sq', 'am']:
        par_text = translator.translate(in_text, dest=i).text
        phrased.append(translator.translate(par_text, dest='en').text.capitalize())
    t = [i for i in phrased if i.lower() != in_text.lower()]
    return "No possible phrases" if not list(set(t)) else list(set(t))
