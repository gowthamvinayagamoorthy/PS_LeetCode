void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int a=m-1;
    int b=n-1;
    int t=m+n-1;
    while(a>=0 && b>=0){
        if (nums1[a]>nums2[b]){
            nums1[t]=nums1[a];
            a-=1;
        }
        else{
            nums1[t]=nums2[b];
            b-=1;
        }
        t-=1;
    }
    while(b>=0){
        nums1[t]=nums2[b];
        b-=1;
        t-=1;
    }
}