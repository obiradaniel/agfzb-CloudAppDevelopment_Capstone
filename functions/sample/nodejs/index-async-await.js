/**
 * Get all dealerships
 */

 const Cloudant = require('@cloudant/cloudant');


 async function main(params) {
     const cloudant = Cloudant({
         url: params.COUCH_URL,
         plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } }
     });
 
 
     try {
         let dbList = await cloudant.db.list();
         return { "dbs": dbList };
     } catch (error) {
         return { error: error.description };
     }
 
 }

 vars = {
    COUCH_URL: "https://bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix.cloudantnosqldb.appdomain.cloud",
IAM_API_KEY:"Tq5P17CW558thKdS_1lV3Y1JGIcB7q8yVylP9EBlpNfH",
COUCH_USERNAME: "bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix"
}

d=main(vars)
console.log(d)