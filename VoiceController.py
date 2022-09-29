import VoiceService
import ZamzarService


def route(file_name):
    if not str(file_name).endswith('.wav'):
        file_name = ZamzarService.route(file_name)
    star, message = VoiceService.speeach_to_texto(file_name)
    return star, message
