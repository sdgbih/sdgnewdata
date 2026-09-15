from sdg.open_sdg import open_sdg_build
from sdg.translations import TranslationHelper

_original_translate = TranslationHelper.translate

def translate_without_sdmx_codes(self, text, language, default_group=None):
    if isinstance(default_group, list) and default_group:
        if default_group[0] in ['SERIES', 'UNIT_MEASURE']:
            return text
    return _original_translate(self, text, language, default_group)

TranslationHelper.translate = translate_without_sdmx_codes

open_sdg_build(config='config_data.yml')
