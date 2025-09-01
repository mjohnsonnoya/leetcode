#include <vector>
#include <queue>
#include <climits>
using namespace std;

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        const int INF = m * n;
        vector<vector<int>> dist(m, vector<int>(n, INF));
        queue<pair<int,int>> q;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {        // note: j < n (not i < n)
                if (mat[i][j] == 0) {
                    dist[i][j] = 0;
                    q.emplace(i, j);
                }
            }
        }

        // 4-neighborhood
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

        // BFS
        while (!q.empty()) {
            auto [i, j] = q.front(); q.pop();
            for (auto& d : dirs) {
                int ni = i + d[0], nj = j + d[1];
                if (0 <= ni && ni < m && 0 <= nj && nj < n &&
                    dist[ni][nj] > dist[i][j] + 1) {
                    dist[ni][nj] = dist[i][j] + 1;
                    q.emplace(ni, nj);
                }
            }
        }
        return dist;
    }
};

