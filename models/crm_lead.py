from odoo import models, fields, api
import requests

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    latitude = fields.Float(string="Latitude")
    longitude = fields.Float(string="Longitude")
    location_address = fields.Char(string="Location Address")

    @api.model
    def create(self, vals):
        lead = super(CRMLead, self).create(vals)
        if vals.get('latitude') and vals.get('longitude'):
            lead._compute_location_address()
        return lead

    def write(self, vals):
        res = super(CRMLead, self).write(vals)
        if vals.get('latitude') and vals.get('longitude'):
            self._compute_location_address()
        return res

    def _compute_location_address(self):
        for lead in self:
            if lead.latitude and lead.longitude:
                try:
                    response = requests.get(
                        'https://nominatim.openstreetmap.org/reverse',
                        params={
                            'format': 'json',
                            'lat': lead.latitude,
                            'lon': lead.longitude,
                            'zoom': 18,
                            'addressdetails': 1
                        },
                        headers={'User-Agent': 'Odoo CRM Location Tracker'}
                    )
                    if response.status_code == 200:
                        data = response.json()
                        lead.location_address = data.get('display_name')
                except Exception:
                    lead.location_address = 'Address not found'


    def action_open_google_map(self):
        for lead in self:
            if lead.latitude and lead.longitude:
                url = f"https://www.google.com/maps?q={lead.latitude},{lead.longitude}"
                return {
                    'type': 'ir.actions.act_url',
                    'name': 'Google Maps',
                    'target': 'new',
                    'url': url
                }
