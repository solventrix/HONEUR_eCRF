from opal.core import episodes
from opal.core import application


class LineOfTreatmentEpisode(episodes.EpisodeCategory):
    display_name = "Treatment Line"
    detail_template = "detail/treatmentline.html"


# class FollowUpEpisode(episodes.EpisodeCategory):
#     display_name = "Treatment Line"
#     detail_template = "detail/followup.html"
