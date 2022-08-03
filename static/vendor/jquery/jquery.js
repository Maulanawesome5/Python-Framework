$('[data-bs-toggle="tooltip"]').tooltip() // to enable tooltips, with default configuration

$('[data-bs-toggle="tooltip"]').tooltip({ boundary: 'clippingParents', customClass: 'myClass' }) // to initialize tooltips with given configuration

$('#myTooltip').tooltip('show') // to trigger `show` method
