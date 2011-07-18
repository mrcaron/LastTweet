# Created by Michael Caron on 2010-01-21.
# Copyright (c) 2009 Michael Caron. All rights reserved.

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import system_message
from trac.util.html import html as tag
import twitter

class LatestTweetMacro(WikiMacroBase):
    """A small maco for showing a users's latest tweet."""
    
    def render_macro(self, req, name, content):
        content = content.strip()
        #return tag.script('', src=self.SCRIPT_LOCATION%content, type='text/javascript')
        statuses = twitter.Api().GetUserTimeline(content)
	return tag.span("Said " + statuses[0].GetRelativeCreatedAt() + ": \"" + statuses[0].text + "\"", class_="tweet")



