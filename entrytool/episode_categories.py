from opal.core import episodes


class Default(episodes.EpisodeCategory):
    display_name = "Default"
    detail_template = "default.html"


class LineOfTreatmentEpisode(episodes.EpisodeCategory):
    display_name = "Treatment Line"
    detail_template = "detail/treatmentline.html"

