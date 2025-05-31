{
    "name": "CRM Location Tracker (Community - Odoo 18)",
    "version": "1.0",
    "depends": ["crm"],
    "summary": "Track salesperson location when creating CRM leads (Odoo 18 Community Edition).",
    "description": "Captures GPS location when creating leads and adds a map link button.",
    "data": [
        "views/crm_lead_views.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "crm_location_tracker_community_odoo18/static/src/js/crm_location.js"
        ]
    },
    "installable": True,
    "auto_install": False,
    "application": False
}
