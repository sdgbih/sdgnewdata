from sdg.open_sdg import open_sdg_build
from sdg.Indicator import Indicator
from sdg.ProgressMeasure import IndicatorProgress


# Keep the original translation behavior.
_original_translate = Indicator.translate


def translate_with_progress_source(self, language, translation_helper):
    _original_translate(self, language, translation_helper)

    translated_indicator = self.translations.get(language)

    if translated_indicator is not None:
        translated_indicator._progress_source = self


Indicator.translate = translate_with_progress_source


# Keep the original ProgressMeasure initialization.
_original_progress_init = IndicatorProgress.__init__


def progress_init_with_original_indicator(
    self,
    indicator,
    logging=None,
    cache_store=None
):
    # Progress must use the untranslated data because
    # SERIES and UNIT_MEASURE are translated for presentation.
    progress_source = getattr(indicator, '_progress_source', indicator)

    _original_progress_init(
        self,
        progress_source,
        logging=logging,
        cache_store=cache_store
    )


IndicatorProgress.__init__ = progress_init_with_original_indicator


open_sdg_build(config='config_data.yml')



