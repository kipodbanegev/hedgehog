var notempty = {
    validators: {
        notEmpty: {
            message: 'זהו שדה חובה'
        }
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
        event_name: notempty,
        event_place: notempty,
        event_date: notempty,
        event_time: notempty,
        event_time_end: notempty
    }
}

function get_today() {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10) {
        dd='0'+dd
    }

    if(mm<10) {
        mm='0'+mm
    }

    return dd+'/'+mm+'/'+yyyy;
}

$(document).ready(function() {
    $('#eventForm').bootstrapValidator(validator).on('success.form.bv', function(e) {
	// Prevent form submission
        //e.preventDefault();
        //alert('ok');
    });
    //$('#event_date').datetimepicker({pickTime: false});
    $('#event_date').datetimepicker({sideBySide: true, format: 'DD/MM/YYYY HH:mm', pick12HourFormat: false, minDate:get_today(),language:'he'});
    $('#event_time').datetimepicker({pickDate: false});
    $('#event_time_end').datetimepicker({pickDate: false});
    $('[autofocus]:first').focus();
});