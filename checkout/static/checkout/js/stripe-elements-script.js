$(document).ready(function() {
    var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    var clientSecret = $('#id_client_secret').text().slice(1, -1);
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();
    var card = elements.create('card', {style: style});
    var errorDiv = $('#card-errors');
    var style = {
        base: {
            color: '#212529',
            fontFamily: '"Quicksand", sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    card.mount('#card-element');

    // Display error messages for Stripe Payments input
    card.addEventListener('change', function(e) {

        if (e.error) {
            var added_html = `
                <span>
                    <i class="fa-solid fa-circle-exclamation me-2"></i>
                </span>
                <p>
                    ${e.error.message}
                </p>
            `
            errorDiv.html(added_html);
        } else {
            errorDiv.textContent = '';
        }
    });

    // Handle form submit for Stripe Payments
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        card.update({'disabled': true});
        $('#submit-button').attr('disabled', true);

        var saveInfo = Boolean($('#id_save_info').attr('checked'));
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        var postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
        }
        var url = '/checkout/cache_checkout_data/';
        $.post(url, postData).done(function() {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        email: $.trim(form.email.value),
                        address: {
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            state: $.trim(form.county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        postal_code: $.trim(form.postcode.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                },
            }).then(function(result) {
                if (result.error) {
                    var added_html = `
                        <span>
                            <i class="fa-solid fa-circle-exclamation me-2"></i>
                        </span>
                        <p>
                            ${result.error.message}
                        </p>
                    `
                    errorDiv.html(added_html);
                    $('#payment_form').fadeToggle(100);
                    card.update({'disabled': false});
                    $('#submit-button').attr('disabled', false);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        }).fail(function() {
            location.reload();
        })
    });
});