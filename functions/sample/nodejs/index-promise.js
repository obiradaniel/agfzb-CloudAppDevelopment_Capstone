/**
 * Get all dealerships
 */

const Cloudant = require('@cloudant/cloudant');

function main(params) {

    const cloudant = Cloudant({
        url: params.COUCH_URL,
        plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } }
    });

    let dbListPromise = getDbs(cloudant);
    console.log(dbListPromise);
    return dbListPromise;
}

function getDbs(cloudant) {
    return new Promise((resolve, reject) => {
        cloudant.db.list()
            .then(body => {
                resolve({ dbs: body });
                console.log(body);
            })
            .catch(err => {
                reject({ err: err });
            });
    });
}

vars = {
    COUCH_URL: "https://bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix.cloudantnosqldb.appdomain.cloud",
IAM_API_KEY:"Tq5P17CW558thKdS_1lV3Y1JGIcB7q8yVylP9EBlpNfH"
username: "bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix"
}

console.log(main(vars))