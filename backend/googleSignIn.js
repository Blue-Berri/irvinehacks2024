<script src="https://accounts.google.com/gsi/client" async defer></script>



const REQUEST_CODE_GOOGLE_SIGN_IN = 1; /* unique request id */

function signIn() {
    const request = {
        serverClientId: getString(R.string.server_client_id)
    };

    Identity.getSignInClient(activity)
        .getSignInIntent(request)
        .then(result => {
            try {
                startIntentSenderForResult(
                    result.getIntentSender(),
                    REQUEST_CODE_GOOGLE_SIGN_IN,
                    /* fillInIntent= */ null,
                    /* flagsMask= */ 0,
                    /* flagsValue= */ 0,
                    /* extraFlags= */ 0,
                    /* options= */ null
                );
            } catch (e) {
                console.error("Google Sign-in failed");
            }
        })
        .catch(e => {
            console.error("Google Sign-in failed", e);
        });
}