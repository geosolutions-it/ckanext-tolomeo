// TOLOMEO preview module
ckan.module('tolomeopreview', function (jQuery, _) {
    return {
        initialize: function () {
            var self = this;

            self.el.empty();
            self.el.append($('<div></div>').attr('id', 'mappa'));
            //self.map = ckan.commonLeafletMap('map', this.options.map_config, {center: [0, 0], zoom: 3});

            tolomeo = new TolomeoExt.ToloPanelInter({
//                layout: 'fit',
                withDataPanel: false,
                withToolsPanel: false,
                toolbarOpt: {
                    withPanArrows: true,
                    withQuery: false,
                    withAnnullaSeleziona: false,
                    withSeleziona: false,
                    withIdentify: false,
                    withLegenda: false,
                    withNuovo: false,
                    withUpdateAlfa: false,
                    withAdd: false,
                    withSubtract: false,
                    withAddSub: false,
                    withVertexEdit: false,
                    withDragDrop: false,
                    withDelete: false,
                    withShowCoordinate: false,
                    iconBasePath: '/tolomeo/img/icone/24-default/',
                    defaults: {scale: 'medium'}
                }
            })

            new Ext.Panel({
                title: 'demo tolomeo',
                width: 888,
                height: 400,
                layout: 'fit',
                cls: 'clearCSS',
                renderTo: 'mappa',
                items: [tolomeo]
            });

        }
    };
});
