class Simple{  

    public static void main(String args[]){  

        final int DATA = 36;

        int srcData[]=new int[DATA];
        int histData[]=new int[DATA];

        for(int i = 0; i < DATA; i++){
            histData[i] = 0;
        }

        srcData[0]  = 0; srcData[1]  = 0; srcData[2]  = 1; srcData[3]  = 4; srcData[4]  = 4; srcData[5]  = 5;
        srcData[6]  = 0; srcData[7]  = 1; srcData[8]  = 3; srcData[9]  = 4; srcData[10] = 3; srcData[11] = 4;
        srcData[12] = 1; srcData[13] = 3; srcData[14] = 4; srcData[15] = 2; srcData[16] = 1; srcData[17] = 3;
        srcData[18] = 4; srcData[19] = 4; srcData[20] = 3; srcData[21] = 1; srcData[22] = 0; srcData[23] = 0;
        srcData[24] = 5; srcData[25] = 4; srcData[26] = 2; srcData[27] = 1; srcData[28] = 0; srcData[29] = 0;
        srcData[30] = 5; srcData[31] = 5; srcData[32] = 4; srcData[33] = 3; srcData[34] = 1; srcData[35] = 0;

        int ptr = 0;

        // Calculate histogram
        while (ptr < srcData.length) {
            int h = 0xFF & srcData[ptr];
            histData[h] ++;
            System.out.print(h + "\t");
            if ((ptr + 1) % 6 == 0) {
                System.out.println();
            }
            ptr ++;
        }

        System.out.println("=====Histdata=====");
        System.out.println("Weight 0 is blackest");
        System.out.println("Weight 6 is whitest");

        for (int i = 0; i < 6; i++){
            System.out.println("W " + i + ": " + histData[i]);
        }
        System.out.println("=====Histdata=====");

        // Total number of pixels
        int total = srcData.length;
        
        float sum = 0;
        for (int t=0 ; t<DATA; t++) sum += t * histData[t];

        float sumB = 0;
        int wB = 0;
        int wF = 0;

        float varMax = 0;
        int threshold = 0;

        for (int t=0 ; t<srcData.length; t++) {
            wB += histData[t];               // Weight Background
            System.out.println("wB: " + wB);
            if (wB == 0) continue;

            wF = total - wB;                 // Weight Foreground
            System.out.println("wF: " + wF);
            if (wF == 0) break;

            sumB += (float) (t * histData[t]);  // Cummalitive Sum
            System.out.println("sumB: " + sumB);

            float mB = sumB / wB;            // Mean Background
            System.out.println("mean Background:" + mB);

            float mF = (sum - sumB) / wF;    // Mean Foreground
            System.out.println("mean Foreground:" + mF);

            // Calculate Between Class Variance
            // float varBetween = ((float)wB * (float)wF) / ((mB - mF) * (mB - mF));
            // I think this upper line is incorrect. But concept is clear
            System.out.println(">>" + varBetween);

            // Check if new maximum found
            if (varBetween > varMax) {
                varMax = varBetween;
                threshold = t;
                System.out.println(t);
            }
        }
    System.out.println("Final: " + threshold);
    }  
}  
