# toggl.com Bulk Records Delete

Delete all records for specific timespan from your toggl.com account. If you have ever been worried about your old data, which already not interesting for you, but can be compromized with your account and contain come senstivie information - this script can help to solve this problem.

It will delete all time entries before year ago, which relieves you from worry about it and leaves your recent data untoucned. Please note if you have any team/public activity you should think twice about it, or your client may be confused.

To use this script, just open it and update timespan you want to clear (by default it's from 2001 year to 365 days ago) and specify your toggl email/password. Script is pretty simple and short, so you can be sure it won't be spoiled or sent to 3rd party (until you have https and nobody plays with DNS).

If script died - just run it again, if problem persists - create an issue. If you stop script execution you just can run it again, but some records will be already deleted. It's tend to be sorted by time, oldest first, but I can't rely on that behavior in future.

Script is quite slow, but doesn't take any CPU/memory - just run it in some tab and go on.
