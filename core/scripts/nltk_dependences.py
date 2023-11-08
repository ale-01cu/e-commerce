import nltk

# Instala las dependencias de NLTK
def download_nltk_packages():
    nltk_packages = [
        'stopwords',
        'punkt',
        'wordnet',
    ]

    for package in nltk_packages:
        try:
            nltk.data.find('tokenizers/' + package)
        except LookupError:
            try:
                print("Instalando dependencias de NLTK: " + package)
                nltk.download(package)
                print("Dependencias de NLTK: " + package + " instalada.")

            except:
                print("No se pudo instalar la dependencia: " + package) 