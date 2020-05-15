# (C) 2020 முத்து அண்ணாமலை
# இந்த நிரல் ஓப்பன்-தமிழ் திட்டத்தின் பகுதியாகும்
# மேற்கோள் - https://en.wikipedia.org/wiki/Tamil_All_Character_Encoding

OFFSET=int('0xE200',16)
constFF0F=int('0xFF0F',16)
constFFF0=int('0xFFF0',16)
const000F=int('0x000F',16)

def splitMeiUyir(uyirmei_char):
    uyir = uyirmei_char & constFF0F
    mei = uyirmei_char & constFFF0
    return (mei,uyir)

def joinMeiUyir(mei_char, uyir_char):
    """This function join mei character and uyir character, and retuns as
    compound uyirmei unicode character."""
    return mei_char | (uyir_char & const000F)

#OrderedDict
tace2utf8 = ([
    ("“", "\""),
    ("”", "\""),
    ("‘", "'"),
    ("’", "'"),
    ("", "க்ஷீ"),
    ("", "க்ஷே"),
    ("", "க்ஷை"),
    ("", "க்ஷொ"),
    ("", "க்ஷோ"),
    ("", "ஸ்ரீ"),
    ("", "க்ஷ்"),
    ("", "க்ஷா"),
    ("", "க்ஷி"),
    ("", "க்ஷு"),
    ("", "க்ஷூ"),
    ("", "க்ஷெ"),
    ("", "க்ஷௌ"),
    ("", "க்ஷ"),
    ("", "க்"),
    ("", "ங்"),
    ("", "ச்"),
    ("", "ஞ்"),
    ("", "ட்"),
    ("", "ண்"),
    ("", "த்"),
    ("", "ந்"),
    ("", "ப்"),
    ("", "ம்"),
    ("", "ய்"),
    ("", "ர்"),
    ("", "ல்"),
    ("", "வ்"),
    ("", "ழ்"),
    ("", "ள்"),
    ("", "ற்"),
    ("", "ன்"),
    ("", "ஸ்"),
    ("", "ஷ்"),
    ("", "ஜ்"),
    ("", "ஹ்"),
    ("", "கா"),
    ("", "ஙா"),
    ("", "சா"),
    ("", "ஞா"),
    ("", "டா"),
    ("", "ணா"),
    ("", "தா"),
    ("", "நா"),
    ("", "பா"),
    ("", "மா"),
    ("", "யா"),
    ("", "ரா"),
    ("", "லா"),
    ("", "வா"),
    ("", "ழா"),
    ("", "ளா"),
    ("", "றா"),
    ("", "னா"),
    ("", "ஸா"),
    ("", "ஷா"),
    ("", "ஜா"),
    ("", "ஹா"),
    ("", "கி"),
    ("", "ஙி"),
    ("", "சி"),
    ("", "ஞி"),
    ("", "டி"),
    ("", "ணி"),
    ("", "தி"),
    ("", "நி"),
    ("", "பி"),
    ("", "மி"),
    ("", "யி"),
    ("", "ரி"),
    ("", "லி"),
    ("", "வி"),
    ("", "ழி"),
    ("", "ளி"),
    ("", "றி"),
    ("", "னி"),
    ("", "ஸி"),
    ("", "ஷி"),
    ("", "ஜி"),
    ("", "ஹி"),
    ("", "கீ"),
    ("", "ஙீ"),
    ("", "சீ"),
    ("", "ஞீ"),
    ("", "டீ"),
    ("", "ணீ"),
    ("", "தீ"),
    ("", "நீ"),
    ("", "பீ"),
    ("", "மீ"),
    ("", "யீ"),
    ("", "ரீ"),
    ("", "லீ"),
    ("", "வீ"),
    ("", "ழீ"),
    ("", "ளீ"),
    ("", "றீ"),
    ("", "னீ"),
    ("", "ஸீ"),
    ("", "ஷீ"),
    ("", "ஜீ"),
    ("", "ஹீ"),
    ("", "கு"),
    ("", "ஙு"),
    ("", "சு"),
    ("", "ஞு"),
    ("", "டு"),
    ("", "ணு"),
    ("", "து"),
    ("", "நு"),
    ("", "பு"),
    ("", "மு"),
    ("", "யு"),
    ("", "ரு"),
    ("", "லு"),
    ("", "வு"),
    ("", "ழு"),
    ("", "ளு"),
    ("", "று"),
    ("", "னு"),
    ("", "ஸு"),
    ("", "ஷு"),
    ("", "ஜு"),
    ("", "ஹு"),
    ("", "கூ"),
    ("", "ஙூ"),
    ("", "சூ"),
    ("", "ஞூ"),
    ("", "டூ"),
    ("", "ணூ"),
    ("", "தூ"),
    ("", "நூ"),
    ("", "பூ"),
    ("", "மூ"),
    ("", "யூ"),
    ("", "ரூ"),
    ("", "லூ"),
    ("", "வூ"),
    ("", "ழூ"),
    ("", "ளூ"),
    ("", "றூ"),
    ("", "னூ"),
    ("", "ஸூ"),
    ("", "ஷூ"),
    ("", "ஜூ"),
    ("", "ஹூ"),
    ("", "கெ"),
    ("", "ஙெ"),
    ("", "செ"),
    ("", "ஞெ"),
    ("", "டெ"),
    ("", "ணெ"),
    ("", "தெ"),
    ("", "நெ"),
    ("", "பெ"),
    ("", "மெ"),
    ("", "யெ"),
    ("", "ரெ"),
    ("", "லெ"),
    ("", "வெ"),
    ("", "ழெ"),
    ("", "ளெ"),
    ("", "றெ"),
    ("", "னெ"),
    ("", "ஸெ"),
    ("", "ஷெ"),
    ("", "ஜெ"),
    ("", "ஹெ"),
    ("", "கே"),
    ("", "ஙே"),
    ("", "சே"),
    ("", "ஞே"),
    ("", "டே"),
    ("", "ணே"),
    ("", "தே"),
    ("", "நே"),
    ("", "பே"),
    ("", "மே"),
    ("", "யே"),
    ("", "ரே"),
    ("", "லே"),
    ("", "வே"),
    ("", "ழே"),
    ("", "ளே"),
    ("", "றே"),
    ("", "னே"),
    ("", "ஸே"),
    ("", "ஷே"),
    ("", "ஜே"),
    ("", "ஹே"),
    ("", "கை"),
    ("", "ஙை"),
    ("", "சை"),
    ("", "ஞை"),
    ("", "டை"),
    ("", "ணை"),
    ("", "தை"),
    ("", "நை"),
    ("", "பை"),
    ("", "மை"),
    ("", "யை"),
    ("", "ரை"),
    ("", "லை"),
    ("", "வை"),
    ("", "ழை"),
    ("", "ளை"),
    ("", "றை"),
    ("", "னை"),
    ("", "ஸை"),
    ("", "ஷை"),
    ("", "ஜை"),
    ("", "ஹை"),
    ("", "கொ"),
    ("", "ஙொ"),
    ("", "சொ"),
    ("", "ஞொ"),
    ("", "டொ"),
    ("", "ணொ"),
    ("", "தொ"),
    ("", "நொ"),
    ("", "பொ"),
    ("", "மொ"),
    ("", "யொ"),
    ("", "ரொ"),
    ("", "லொ"),
    ("", "வொ"),
    ("", "ழொ"),
    ("", "ளொ"),
    ("", "றொ"),
    ("", "னொ"),
    ("", "ஸொ"),
    ("", "ஷொ"),
    ("", "ஜொ"),
    ("", "ஹொ"),
    ("", "கோ"),
    ("", "ஙோ"),
    ("", "சோ"),
    ("", "ஞோ"),
    ("", "டோ"),
    ("", "ணோ"),
    ("", "தோ"),
    ("", "நோ"),
    ("", "போ"),
    ("", "மோ"),
    ("", "யோ"),
    ("", "ரோ"),
    ("", "லோ"),
    ("", "வோ"),
    ("", "ழோ"),
    ("", "ளோ"),
    ("", "றோ"),
    ("", "னோ"),
    ("", "ஸோ"),
    ("", "ஷோ"),
    ("", "ஜோ"),
    ("", "ஹோ"),
    ("", "கௌ"),
    ("", "ஙௌ"),
    ("", "சௌ"),
    ("", "ஞௌ"),
    ("", "டௌ"),
    ("", "ணௌ"),
    ("", "தௌ"),
    ("", "நௌ"),
    ("", "பௌ"),
    ("", "மௌ"),
    ("", "யௌ"),
    ("", "ரௌ"),
    ("", "லௌ"),
    ("", "வௌ"),
    ("", "ழௌ"),
    ("", "ளௌ"),
    ("", "றௌ"),
    ("", "னௌ"),
    ("", "ஸௌ"),
    ("", "ஷௌ"),
    ("", "ஜௌ"),
    ("", "ஹௌ"),
    ("", "அ"),
    ("", "ஆ"),
    ("", "இ"),
    ("", "ஈ"),
    ("", "உ"),
    ("", "ஊ"),
    ("", "எ"),
    ("", "ஏ"),
    ("", "ஐ"),
    ("", "ஒ"),
    ("", "ஓ"),
    ("", "ஔ"),
    ("", "ஃ"),
    ("", "க"),
    ("", "ங"),
    ("", "ச"),
    ("", "ஞ"),
    ("", "ட"),
    ("", "ண"),
    ("", "த"),
    ("", "ந"),
    ("", "ப"),
    ("", "ம"),
    ("", "ய"),
    ("", "ர"),
    ("", "ல"),
    ("", "வ"),
    ("", "ழ"),
    ("", "ள"),
    ("", "ற"),
    ("", "ன"),
    ("", "ஸ"),
    ("", "ஷ"),
    ("", "ஜ"),
    ("", "ஹ"),
    ])
