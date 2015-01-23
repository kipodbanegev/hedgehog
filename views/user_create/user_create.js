var email_validator = {
    validators: {
        notEmpty: {
            message: 'זהו שדה חובה'
        },
	emailAddress: {
            message: 'כתובת דואר אלקטרוניז זו אינה תקינה'
        },
    }
}

var password_validator = {
    validators: {
        notEmpty: {
            message: 'זהו שדה חובה'
        },
        stringLength: {
            min: 5,
            max: 30,
            message: 'הססמה חייבת להיות לפחות באורך 5 תווים ולא פחות מ-30 תווים'
        },
    }
}


var validator = {
    message: 'This value is not valid',
    feedbackIcons: {
	valid: 'glyphicon glyphicon-ok',
	invalid: 'glyphicon glyphicon-remove',
	validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        email: email_validator,
        password: password_validator,
    }
}

$(document).ready(function() {
    $('#user_create_form').bootstrapValidator(validator).on('success.form.bv', function(e){});
    $('[autofocus]:first').focus();
});