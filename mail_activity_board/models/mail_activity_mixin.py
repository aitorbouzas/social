# Copyright 2016 David Juaneda - <djuaneda@sdi.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, api, _


class MailActivityMixin(models.AbstractModel):
    _inherit = 'mail.activity.mixin'

    def redirect_to_activities(self, **kwargs):
        """
            Redirects to the list of activities of the object shown.

            Redirects to the activity board and configures the domain so that
            only those activities that are related to the object shown are
            displayed.

            Add to the title of the view the name the class of the object from
            which the activities will be displayed.

            :param kwargs: Dictionary that contains the id of the object
                            and the model it is about.
            :return: action.
        """
        id = kwargs.get("id")
        action = self.env['mail.activity'].action_activities_board()
        views = []
        for v in action['views']:
            if v[1] == 'tree':
                v = (v[0], 'list')
            views.append(v)
        action['views'] = views
        action['domain'] = [('res_id', '=', id)]
        return action
