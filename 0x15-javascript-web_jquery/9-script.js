$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (req, res) {
    if (res === 'success') {
        $('#hello').text(req.hello);
    }
});