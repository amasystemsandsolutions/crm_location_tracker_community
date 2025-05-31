odoo.define('crm_location_tracker_community.crm_location', function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        _onLoaded: function () {
            this._super.apply(this, arguments);

            if (this.modelName === 'crm.lead') {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition((position) => {
                        const lat = position.coords.latitude;
                        const lon = position.coords.longitude;

                        this.model.set(this.handle, {
                            latitude: lat,
                            longitude: lon
                        });
                    });
                }
            }
        },
    });
});
