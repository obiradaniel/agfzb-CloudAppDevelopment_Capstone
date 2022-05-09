/**
 * Get all dealerships
 */

const Cloudant = require('@cloudant/cloudant');

function main(params) {

    const cloudant = Cloudant({
        url: params.COUCH_URL,
        plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } }
    });

    let dbList = getDbs(cloudant);
    return { dbs: dbList };
}

function getDbs(cloudant) {
    let dbList = []
    cloudant.db.list().then((body) => {
        body.forEach((db) => {
            dbList.push(db);
        });
    }).catch((err) => { console.log(err); });
}

vars = {
    COUCH_URL: "https://bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix.cloudantnosqldb.appdomain.cloud",
IAM_API_KEY:"Tq5P17CW558thKdS_1lV3Y1JGIcB7q8yVylP9EBlpNfH"
}

console.log(main(vars))