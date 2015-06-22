function registerUploadForm(form) {

  var doc_file = form.find("input[name='doc_file']");

  doc_file.change(function (evt){
    // Selecting what we need from the UI
    var status = $('.status');
    var parent_form = $(evt.target.form);
    var input_file = $(evt.target);
    var submit_btn = parent_form.find('input[type="submit"]');
    var file_name = parent_form.find("input[name='file_name']");

    if (evt.target.files.length === 0) {
      // deselecting a file
      status.text('Waiting for file.');
      input_file.val('');
      file_name.val('');
      return;
    }

    var file = evt.target.files[0];

    var filename = file.name;

    // first we need to get signature for authorization
    $.ajax('/example/documents/s3auth/?' + 'file_name=' + filename).done(function (data) {
      // now we can construct the payload with the signature
      var fd = new FormData();

      for (var key in data.form_args.fields) {
        if (data.form_args.fields.hasOwnProperty(key)) {
          console.log(key, data.form_args.fields[key]);
          fd.append(key, data.form_args.fields[key]);
        }
      }
      fd.append('file', evt.target.files[0]);



      // feedback that we are uploading the file
      status.html('Uploading file please wait...');
      input_file.prop('disabled', true);
      submit_btn.prop('disabled', true);
      $.ajax({method: "POST",
             url: data.form_args.action,
             data: fd,
             processData: false,
             contentType: false,
             success: function(){
               status.html('File uploaded, press submit to save.');
               // set the hidden field to the uploaded file's path
               file_name.val(data.file_path);
             },
             error: function(){
               status.html('Error.');
               // clear the field so the user can try again.
               input_file.val('');
               file_name.val('');
             },
             complete: function (){
               // re-enable the input field once completed.
               input_file.prop('disabled', false);
               submit_btn.prop('disabled', false);
             }
      });
    });
  });

  form.submit(function(evt) {
    var parent_form = $(evt.target);
    var file_name = parent_form.find("input[name='file_name']");
    var input_file = parent_form.find("input[name='doc_file']");
    if (file_name.val()) {
      // remove file from input so it doesn't get uploaded
      // on submit of the form.
      input_file.val('');
    }
  });

}
