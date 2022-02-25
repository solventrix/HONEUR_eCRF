from opal.core import episodes


class Default(episodes.EpisodeCategory):
    """
    This is the default episode category of any episode.

    It exists because, in Opal, an episode must have an
    episode_category.

    In this application the pathway to add an episode should
    always assign a condition category e.g. MM or CLL after the
    episode has been created. IE we should not see any episodes
    with this category name.
    """
    display_name = "Default"


class LineOfTreatmentEpisode(episodes.EpisodeCategory):
    display_name = "Treatment Line"
