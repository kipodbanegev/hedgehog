var validator = {
    message: 'This value is not valid',
    feedbackIcons: {
	valid: 'glyphicon glyphicon-ok',
	invalid: 'glyphicon glyphicon-remove',
	validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        event_name: {
	    validators: {
                notEmpty: {
	            message: 'The username is required and cannot be empty'
	        }
	    }
	}
    }
}

$(document).ready(function() {
    $('#eventForm').bootstrapValidator(validator).on('success.form.bv', function(e) {
	// Prevent form submission
        e.preventDefault();
        alert('ok');
    });
});