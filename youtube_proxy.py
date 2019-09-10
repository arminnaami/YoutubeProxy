from youtube_transcript_api import YouTubeTranscriptApi

def obtener_transcripcion_video(id_video):
    """
    Obtiene la transcripcion de un video, dado su id.
    Retorna una cadena.
    """

    # Obtener la lista de subtitulos en espanol
    subtitulos = YouTubeTranscriptApi.get_transcript(id_video, languages=['es'])

    # Cadena en donde se concatenaran los subtitulos
    transcripcion = ''

    # Recorrer subtitulos y concatenarlos
    for s in subtitulos:
        transcripcion += s['text'] + ' '

    # Retornar la transcripcion
    return transcripcion

def obtener_transcripciones_videos(ids_videos):
    """
    Obtiene las transcripciones de varios videos, dados sus ids.
    Retorna un diccionario, donde las llaves son los ids, y los valores son cadenas.
    """

    # Obtener las listas de subtitulos en espanol
    diccionario_subtitulos = YouTubeTranscriptApi.get_transcripts(ids_videos, languages=['es'])[0]

    # Diccionario en donde se concatenaran los subtitulos por cada id
    diccionario_transcripciones = dict()

    # Recorrer el diccionario de subtitulos
    for id in diccionario_subtitulos.keys():
        # Cadena temporal donde se concatenaran los subtitulos para un id
        transcripcion = ''

        # Recorrer la lista de subtitulos para un id y concatenarlos
        for s in diccionario_subtitulos[id]:
            transcripcion += s['text'] + ' '

        # Guardar el resultado en el diccionario de transcripciones
        diccionario_transcripciones[id] = transcripcion

    # Retornar el diccionario de transcripciones
    return diccionario_transcripciones



# Prueba para un video
print(obtener_transcripcion_video('03KCoeXbMuY'))

# Prueba para varios videos
print(obtener_transcripciones_videos(['03KCoeXbMuY', 'wilWvq3CvOM', '2oIrhbXcmgI']))