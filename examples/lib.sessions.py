from mwutil.api import Session
from mwutil.lib import sessions

# Gather a user's revisions from the API
api_session = Session("https://en.wikipedia.org/w/api.php")
revs = api_session.user_contribs.query(
	user={"TestAccountForMWUtils"}, 
	direction="newer"
)
rev_events = ((rev['user'], rev['timestamp'], rev) for rev in revs)

# Extract and print sessions
for user, session in sessions.cluster(rev_events):
	print("{0}'s session with {1} revisions".format(user, len(session)))