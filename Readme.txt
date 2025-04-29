#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

const int MAX = 1005;

vector<pair<int, int>> graph[MAX]; // node -> (neighbor, time)
int dist[MAX];

int main() {
    int nodes, edges;
    cin >> nodes >> edges;

    for (int i = 0; i < edges; ++i) {
        int u, v, time;
        cin >> u >> v >> time;
        graph[u].push_back({v, time});
        graph[v].push_back({u, time}); // undirected
    }

    int k; // number of emergency stations
    cin >> k;
    vector<int> emergency(k);
    for (int i = 0; i < k; ++i) {
        cin >> emergency[i];
    }

    int incident;
    cin >> incident;

    // Set all distances to infinity
    for (int i = 1; i <= nodes; ++i)
        dist[i] = INT_MAX;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;

    // Push all emergency stations with 0 distance
    for (int src : emergency) {
        dist[src] = 0;
        pq.push({0, src});
    }

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, t] : graph[u]) {
            if (dist[v] > dist[u] + t) {
                dist[v] = dist[u] + t;
                pq.push({dist[v], v});
            }
        }
    }

    if (dist[incident] == INT_MAX)
        cout << "No path to incident.\n";
    else
        cout << "Fastest time to incident: " << dist[incident] << endl;

    return 0;
}
