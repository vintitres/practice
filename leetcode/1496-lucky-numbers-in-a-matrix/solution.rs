impl Solution {
    pub fn lucky_numbers (matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut row_min : Vec<i32> = matrix.iter().map(|row|
            *row.iter().min().unwrap()
        ).collect();
        let col_max : Vec<i32> = (0..matrix[0].len()).map(|j|
            (0..matrix.len()).map(|i| matrix[i][j]).max().unwrap()
        ).collect();
        let mut lucky = Vec::new();
        for i in 0..matrix.len() {
            for j in 0..matrix[i].len() {
                if matrix[i][j] == row_min[i] && matrix[i][j] == col_max[j] {
                    lucky.push(matrix[i][j]);
                }
            }
        }
        lucky
    }
}
