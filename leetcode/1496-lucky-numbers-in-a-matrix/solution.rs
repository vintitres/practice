impl Solution {
    pub fn lucky_numbers (matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut row_min : Vec<i32> = Vec::new();
        let mut col_max = Vec::new();
        for i in 0..matrix.len() {
            row_min.push(*matrix[i].iter().min().unwrap());
        }
        for j in 0..matrix[0].len() {
            col_max.push(
                (0..matrix.len()).map(|i| matrix[i][j]).max().unwrap(),
            );
        }
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
