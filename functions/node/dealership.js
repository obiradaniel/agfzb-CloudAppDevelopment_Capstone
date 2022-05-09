
function main(params) { 
    
vars = {
    COUCH_URL: "https://bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix.cloudantnosqldb.appdomain.cloud",
IAM_API_KEY:"Tq5P17CW558thKdS_1lV3Y1JGIcB7q8yVylP9EBlpNfH",
COUCH_USERNAME: "bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix"
}

   //console.log(params); 
   return new Promise(function (resolve, reject) { 
       const Cloudant = require('@cloudant/cloudant'); 
       const cloudant = Cloudant({ 
           url: vars.COUCH_URL, 
           plugins: {iamauth: {iamApiKey:vars.IAM_API_KEY}} 
       }); 
       const dealershipDb = cloudant.use('dealerships'); 
    if (params.state) { 
        // return dealership with this state
        state = String(params.state)
        dealershipDb.find({
        "selector": 
            //{"st": state},
            {"st": { "$eq":state }},
            "fields": ["id","city", "state", "st", "address", "zip", 
            "lat", "long", "short_name", "full_name"],
            /**"limit":1
               "sort": [
                  {
                     "id": "asc"
                  }
               ],
               "use_index": "db_index"**/
        }, 
        function (err, result) { 
                if (err) { 
                   console.log("🚀 ~ file: index.js ~ line 20 ~ err", err) 
                   reject(err); 
               } 
               let code=200; 
                   if (result.docs.length==0) 
                   { 
                   code= 404; 
                   } 
               resolve({ 
                   statusCode: code, 
                   headers: { 'Content-Type': 'application/json' }, 
                   body: result 
               }); 
           }); 
        } 
    else if (params.id) { 
           id=parseInt(params.id) 
         // return dealership with this state 
           dealershipDb.find({
        "selector": 
            {
            "id": id
            },
            "fields": [
                "id",
                "city",
                "state",
                "st",
                "address",
                "zip",
                "lat",
                "long",
                "short_name",
                "full_name"
                   ]
               //,"use_index": "db_index"
        }, function (err, result) { 
               if (err) { 
                  console.log("🚀 ~ file: index.js ~ line 20 ~ err", err) 
                   reject(err); 
               } 
               let code=200; 
                   if (result.docs.length==0) 
                   { 
                   code= 404; 
                   } 
        resolve({ 
                   statusCode: code, 
                   headers: { 'Content-Type': 'application/json' }, 
                   body: result 
               }); 
           }); 
       } 
    else { 
           // return all documents 
         dealershipDb.list({ include_docs: true }, function (err, result) { 
               if (err) { 
                   console.log("🚀 ~ file: index.js ~ line 35 ~ err", err) 
        reject(err); 
               } 
            resolve({ 
                   statusCode: 200, 
                   headers: { 'Content-Type': 'application/json' }, 
                   body: result 
               })
            console.log(result) ; 
           }); 
       } 
   }); 
}