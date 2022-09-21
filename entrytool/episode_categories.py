from opal.core import episodes


class Default(episodes.EpisodeCategory):
    """
    This is the default episode category of any episode.

    In Opal, an episode must have a value in the field `category_name` 
    that relates to an `EpisodeCategory` class.

    In this application any episode that is initially assigned the
    default at episode creation time should then be assigned to the
    appropriate category e.g. an MM or CLL episode before the transaction
    commits.

    Any episodes that exist in the database with 'Default' as their
    `category_name` likely exist in error and should be investigated.
    """
    display_name = "Default"


class LineOfTreatmentEpisode(episodes.EpisodeCategory):
    display_name = "Treatment Line"
