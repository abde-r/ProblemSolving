use std::io;
// use rand::Rng;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

// Board is represented as a 3x3 array (0 means empty, 1–6 are dice values)
type Board = [[u8; 3]; 3];

/// Compute the hash of a board state by iterating left-to-right, top-to-bottom.
/// The algorithm shifts the current hash by one decimal digit (i.e. multiplies by 10) and adds the cell value.
fn board_hash(board: &Board) -> u32 {
    let mut hash: u32 = 0;
    for row in board.iter() {
        for &cell in row.iter() {
            hash = hash * 10 + (cell as u32);
        }
    }
    hash
}

/// Check if a move is possible on the board.
/// In this game, a move is possible if there is at least one empty cell (0).
fn moves_available(board: &Board) -> bool {
    board.iter().any(|row| row.iter().any(|&cell| cell == 0))
}

/// Return all possible moves from a given board state as new board states.
/// For each empty cell, we simulate placing a die:
///   - If a capturing move is possible at that cell, simulate each possible capture (and update the placed die’s value).
///   - Otherwise, place a die with value 1.
fn simulate_moves(board: &Board) -> Vec<Board> {
    let mut next_states = Vec::new();
    // let mut rng = rand::thread_rng();

    // For each empty cell (i, j)
    for i in 0..3 {
        for j in 0..3 {
            if board[i][j] == 0 {
                // Create a copy of the board to simulate a move.
                let mut new_board = *board;
                // Check for capturing move: 
                // Here, we check the four cardinal adjacents (you can adjust to include diagonals if needed)
                let adjacent_positions = adjacent_positions(i, j, 3, 3);
                // Compute sum of adjacent dice (only consider nonzero cells)
                let mut capture_sum = 0;
                for (ni, nj) in &adjacent_positions {
                    if new_board[*ni][*nj] != 0 {
                        capture_sum += new_board[*ni][*nj];
                    }
                }
                if capture_sum > 0 && capture_sum <= 6 {
                    // Capturing placement: remove the adjacent dice and place a die with the capture sum.
                    for (ni, nj) in &adjacent_positions {
                        if new_board[*ni][*nj] != 0 {
                            new_board[*ni][*nj] = 0;
                        }
                    }
                    new_board[i][j] = capture_sum;
                    // In a full implementation, if multiple capture combinations are possible,
                    // you would generate one new state for each possible capture.
                    next_states.push(new_board);
                } else {
                    // Non-capturing placement: simply place a 1.
                    new_board[i][j] = 1;
                    next_states.push(new_board);
                }
            }
        }
    }
    next_states
}

/// Given a board state and a maximum number of turns,
/// simulate all possible games from that state and return a vector of final board hashes.
fn simulate_games(board: &Board, turns_remaining: i32) -> Vec<u32> {
    // If no moves can be made or turns are exhausted, compute hash.
    if turns_remaining == 0 || !moves_available(board) {
        return vec![board_hash(board)];
    }

    let mut final_hashes = Vec::new();
    // For each possible move from the current board...
    for next_board in simulate_moves(board) {
        // Recurse with one less turn.
        let mut hashes = simulate_games(&next_board, turns_remaining - 1);
        final_hashes.append(&mut hashes);
    }
    final_hashes
}

/// Helper: returns the four cardinal adjacent positions (top, bottom, left, right)
fn adjacent_positions(i: usize, j: usize, rows: usize, cols: usize) -> Vec<(usize, usize)> {
    let mut positions = Vec::new();
    // Up
    if i > 0 {
        positions.push((i - 1, j));
    }
    // Down
    if i + 1 < rows {
        positions.push((i + 1, j));
    }
    // Left
    if j > 0 {
        positions.push((i, j - 1));
    }
    // Right
    if j + 1 < cols {
        positions.push((i, j + 1));
    }
    positions
}


fn hash_calculator(hash: String) -> i64 {
    let modulo:i64 = 1 << 30;
    let hash: i64 = hash.trim().parse().expect("Invalid integer");
    hash % modulo
}

fn action_player(game_board: Vec<String>) ->i64 {

    // Concatenate board rows into a single string.
    let board_str: String = game_board.join("");
    
    // Collect positions of '0' in the string.
    let positions: Vec<usize> = board_str
        .char_indices()
        .filter(|&(_, c)| c == '0')
        .map(|(i, _)| i)
        .collect();
    let k = positions.len();
    
    let mut results: i64 = 0;
    
    // There are 2^k subsets. We want non-empty proper subsets, so
    // iterate from 1 to 2^k - 2 (which excludes both the empty set (0) and the full set (all bits set)).
    for subset in 1..((1 << k) - 1) {
        // Copy board_str into a mutable vector of bytes.
        let mut new_board = board_str.clone().into_bytes();
        // For each zero position, check if the corresponding bit is set in 'subset'.
        for j in 0..k {
            if (subset >> j) & 1 == 1 {
                new_board[positions[j]] = b'1';
            }
        }
        let hash: String = String::from_utf8(new_board).unwrap();
        eprintln!("state: {}", hash);
        results += hash_calculator(hash);
    }
    results
}

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
fn main() {
    let mut input_line = String::new();
    let mut game_board: Vec<String> = Vec::new();
    let mut result: String = String::new();

    io::stdin().read_line(&mut input_line).unwrap();
    let depth = parse_input!(input_line, i32);
    
    // Contructing a game board based on standard input data
    for _ in 0..3 {
        let mut inputs = String::new();
        io::stdin().read_line(&mut inputs).unwrap();
        eprintln!("input: {}", inputs);
        let row: String = inputs
            .trim()
            .split_whitespace()
            .map(|x| x.parse::<String>().unwrap())
            .collect();
        game_board.push(row);
    }
    eprintln!("depth {}", depth);
    eprintln!("game board {:?}", game_board);
    println!("{:?}", action_player(game_board));

    // let initial_board: Board = [
    //     [060], 060222161 => 160222161 061222161 =>  221444322 | 322444322
    //     [222],
    //     [161],
    // ];
    /*
    [506] 506450064 => 516450064 516451064 516450164 506451064 506450164 506451164 => 921220036 | 951223336
    [450]
    [064]
    */
    // let final_hashes = simulate_games(&initial_board, depth);

    // // Sum the hashes modulo 230
    // let final_sum = final_hashes.iter().fold(0, |acc, &hash| (acc + hash) % 230);
    // eprintln!("{}", final_sum.to_string());
    // println!("221444322");
}

