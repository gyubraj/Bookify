$(document).ready(function() {
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            book_name: {
                validators: {
                        stringLength: {
                        min: 1,
                    },
                        notEmpty: {
                        message: 'Please enter your Book name'
                    }
                }
            },
             writer: {
                validators: {
                     stringLength: {
                        min: 1,
                    },
                    notEmpty: {
                        message: 'Please enter Writer Name'
                    }
                }
            },
			 description: {
                validators: {
                     stringLength: {
                        min: 1,
                    },
                    notEmpty: {
                        message: 'Please enter book description'
                    }
                }
            },
			 actual_price: {
                validators: {
                     stringLength: {
                        min: 1,
                    },
                    notEmpty: {
                        message: 'Please enter Actual Book Price'
                    },
                    regexp: {
                        regexp: /^\d+$/,
                        message: 'enter the amount in number'
                      }
                }
            },
			selling_price: {
                validators: {
                     stringLength: {
                        min: 1,
                    },
                    notEmpty: {
                        message: 'Please enter your selling price'
                    },
                    regexp: {
                        regexp: /^\d+$/,
                        message: 'enter the amount in number'
                      }
                }
            },
            publication: {
                validators: {
                     stringLength: {
                        min: 2,
                    },
                    notEmpty: {
                        message: 'Please enter publication Name'
                    }
                }
            },
            contact_no: {
                validators: {
                  stringLength: {
                        min: 12, 
                        max: 12,
                    notEmpty: {
                        message: 'Please enter your Contact No.'
                     }
                }
            },
			 category: {
                validators: {
                    notEmpty: {
                        message: 'Please select your category'
                    }
                }
            },
                }
            }
        })
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
                $('#contact_form').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});