for input in $(cat testcases); 
do 
curl http://127.0.0.1:5000?input=$input
done