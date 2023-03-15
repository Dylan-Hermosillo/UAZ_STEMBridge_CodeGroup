class Solution {
public:

    //given a vector(int) and a target(int), will return the indeces of 
    //the combination of indeces(cannot be the same) that add up to target
    vector<int> twoSum(vector<int>& nums, int target) {
        //declare vector to store indeces
        vector<int> temp; 
        
        //first itteration throughout the array
        for(int i = 0; i < (nums.size()); ++i){
            int numHolder = nums[i];    //hold a number throughout the array; compare it with other numbers in array

            //second itteration throughout the array 
            for(int j = 0; j < (nums.size()); ++j){
                
                //if the compbination adds up to target, push indeces to a vector and return to function 
                if((numHolder + nums[j] == target) && (i != j)){
                    temp.push_back(i);
                    temp.push_back(j);
                    return temp;
                }
            }
        }

        //else will return an empty vector. 
        return temp;

    }
};
