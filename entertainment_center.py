import media
from fresh_tomatoes import open_movies_page

# Create movie objects here.
# Notes: Storylines are taken from each film's respective google search pages.
#       "Ghost World": https://g.co/kgs/k49FJa
#       "Mean Girls": https://g.co/kgs/R9djXI
#       "Times Square": https://g.co/kgs/BsFFhQ
#       "Truck Turner": https://g.co/kgs/iqDF3g
#       "The Slams": https://g.co/kgs/dd0GXs
#       "Straight Outta Compton": https://g.co/kgs/6ZM8GY
#       Actor's names removed for brevity.
#
#       Lines containg movie posters and trailers may exceed PEP8 standards.
#           These lines could not be shortened.
#
ghost_world = media.Movie(
    "Ghost World",
    """The story of neo-cool Enid and Rebecca who, faced with graduation
    from high school, take a hard look at the world they wryly observe and
    decide what they really want. When Enid takes an interest in the offbeat
    Seymour and Rebecca focuses her attention on their mutual romantic fixation
    Josh, the girls' friendship is forever changed.""",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Ghostworldposter.jpg",
    "https://www.youtube.com/watch?v=rq6AOc0ATnU")

mean_girls = media.Movie(
    "Mean Girls",
    """Teenage Cady Heron was educated in Africa by her scientist parents.
    When her family moves to the suburbs of Illinois, Cady finally gets to
    experience public school and gets a quick primer on the cruel, tacit laws
    of popularity that divide her fellow students into tightly knit cliques.
    She unwittingly finds herself in the good graces of an elite group of cool
    students dubbed \"the Plastics,\" but Cady soon realizes how her shallow
    group of new friends earned this nickname. shallow group of new friends
    earned this nickname.""",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/Mean_Girls_movie.jpg",
    "https://www.youtube.com/watch?v=KAOmTMCtGkI")

times_square = media.Movie("Times Square",
                           """A late-night New York disc jockey follows the
                           punk-rock antics of two runaway teenage girls.""",
                           "https://upload.wikimedia.org/wikipedia/en/4/4d/Times_Square_VideoCover.png",
                           "https://www.youtube.com/watch?v=_YzK4X8OAgU")

truck_turner = media.Movie("Truck Turner",
                           """Bounty hunter Mack "Truck" Turner almost always
                           finds his target, but his latest prize -- a pimp
                           called Gator -- is killed while Turner is chasing him.
                            Gator's girl, Dorinda, vows to avenge his death and
                            offers ownership of her successful call girl
                            operation to anyone who can knock off Turner.
                            Upscale pimp Harvard Blue steps in, upping the ante
                             with professional assassins. Turner, however,
                             isn't going down easily.""",
                           "https://upload.wikimedia.org/wikipedia/en/5/5b/Truck_turnerposter.jpg",
                           "https://www.youtube.com/watch?v=HUHmQ0rfejw")

the_slams = media.Movie(
    "The Slams",
    """After a heist Curtis Hook is caught by the police. In jail various
    people want to know where he stashed the loot. But the places where he
    stashed the loot ($1.500.000) will be demolished so he has to get out of
    jail to get to the dough.""",
    "https://upload.wikimedia.org/wikipedia/en/f/fd/The_Slams.jpg",
    "https://www.youtube.com/watch?v=SeWvvGdJ6I8")


straight_outta_compton = media.Movie(
    "Straight Outta Compton",
    """In 1988, a groundbreaking new group revolutionizes music and pop culture,
    changing and influencing hip-hop forever. N.W.A's first studio album,
    "Straight Outta Compton," stirs controversy with its brutally honest
    depiction of life in Southern Los Angeles. With guidance from veteran
    manager Jerry Heller, band members Ice Cube, Dr. Dre, Eazy-E, DJ Yella and
    MC Ren navigate their way through the industry, acquiring fame, fortune and
    a place in history.""",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Straight_Outta_Compton_poster.jpg",
    "https://www.youtube.com/watch?v=oyoew4T74_w")

# Append each film in a list called 'films'.
films = [ghost_world, mean_girls, times_square, truck_turner, the_slams,
         straight_outta_compton]

# Generate website here
open_movies_page(films)