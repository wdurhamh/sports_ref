from lxml import html
"""We're looking for the following nest of tags:
	(2nd p tag)
	<p class="margin0">
		<span class="bold_text">Height:</span>
		[Height]
		<span class="bold_text">weight:</span>
  		[weight]

....
	<table id="player_per_game" class-"sortable_stats_table">
		<tfoot>
			<tr class="bold_test stat_total">
				(8th td) <td align="right">#field goal percentage
				(18th td) <td align=right">#rebounds per game
				(19th) <td align="right">#assits
				(24th) <td align="right">#points per game
				
 """
"""need points per game, field goal percentage, rebounds per game , assits per game, pick, Height and weight """
class SportsRefParser(object):
    def __init__(self, html_page):
        self.tree = html.fromstring(html_page.text)
        self._get_relevant_data()
        print 'initialized'


    def _get_relevant_data(self):
        points_per_game = self._get_points_per_game()
	#field_goal_percentage = self._get_field_goal_percentage()
        #rbs_per_game = self._get_rbs_per_game()
        #asts_per_game = self._get_asts_per_game()
        #height = self_get_height()
        #weight = self._get_weight()

    def _get_points_per_game(self):
        paragraphs = self.tree.xpath('//p[@class="margin0"]/text()')
        print paragraphs

if __name__ == "__main__":
    print "looks like we have the lib all set up"





