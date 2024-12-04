import numpy as np


class Vertex:
    def __init__(self, name: str, adjacents: list[str]) -> None:
        self.name = name
        self.color = "white"
        self.parent = "nil"
        self.discovery_time = np.inf
        self.finish_time = np.inf
        self.adjacents: list[str] = adjacents

    def copy_for_strongly_connected_components(self) -> "Vertex":
        other = Vertex(name=self.name, adjacents=[])
        other.color = "white"
        other.parent = "nil"
        other.discovery_time = np.inf
        other.finish_time = self.finish_time
        return other

    def __str__(self) -> str:
        return (
            f"Vertex{{\n"
            f"    name: {self.name},\n"
            f"    d : f\n"
            f"    {self.discovery_time} : {self.finish_time},\n"
            f"    adjacents: {self.adjacents}"
            f"}}"
        )

    def __repr__(self) -> str:
        return self.__str__()


class Graph:
    def __init__(self, name: str) -> None:
        self.graph: dict[str, Vertex] = {}
        self.name = name

    def vertices(self, sort: str = "") -> list[Vertex]:
        if sort == "alphabetically":
            return sorted(self.graph.values(), key=lambda x: x.name)
        if sort == "by finish time":
            return sorted(
                self.graph.values(),
                key=lambda x: x.finish_time,
                reverse=True,
            )
        return list(self.graph.values())

    def adjacents(self, vertex: Vertex) -> list[Vertex]:
        return sorted(
            [self.graph[v] for v in self.graph[vertex.name].adjacents],
            key=lambda x: x.name,
        )

    def __getitem__(self, key: str) -> Vertex:
        return self.graph[key]

    def __setitem__(self, key: str, value: Vertex) -> None:
        self.graph[key] = value

    def __delitem__(self, key: str) -> None:
        del self.graph[key]

    def __str__(self) -> str:
        result = f"-- {self.name} Graph --\n"
        for vertex in self.graph.values():
            result += str(vertex) + "\n"
        return result

    def __repr__(self) -> str:
        return self.__str__()

    def transpose(self) -> "Graph":
        transpose = Graph(name=f"{self.name} transpose")
        for vertex in self.graph.values():
            transpose[vertex.name] = vertex.copy_for_strongly_connected_components()

        for vertex in self.graph.values():
            for adjacent in vertex.adjacents:
                transpose[adjacent].adjacents.append(vertex.name)
        return transpose


def dfs(graph: Graph, sort: str = "alphabetically") -> None:
    for u in graph.vertices():
        u.color = "white"
        u.parent = "nil"
    time = 0

    for u in graph.vertices(sort):
        if u.color == "white":
            time = dfs_visit(graph, u, time)


def dfs_visit(graph: Graph, u: Vertex, time: int) -> int:
    time += 1
    u.discovery_time = time
    u.color = "gray"
    for v in graph.adjacents(u):
        if v.color == "white":
            v.parent = u.name
            time = dfs_visit(graph, v, time)
    time += 1
    u.finish_time = time
    u.color = "black"
    return time


def dfs_forest(graph: Graph, sort: str = "alphabetically") -> dict[str, list[str]]:
    for u in graph.vertices():
        u.color = "white"
        u.parent = "nil"
    time = 0
    roots: dict[str, list[str]] = {}

    for u in graph.vertices(sort):
        if u.color == "white":
            time, forest = dfs_forest_visit(graph, u, time)
            roots[u.name] = [u.name, *forest]
    return roots


def dfs_forest_visit(graph: Graph, u: Vertex, time: int) -> tuple[int, list[str]]:
    time += 1
    u.discovery_time = time
    u.color = "gray"
    forest = []
    for v in graph.adjacents(u):
        if v.color == "white":
            v.parent = u.name
            forest.append(v.name)
            time, deep_forest = dfs_forest_visit(graph, v, time)
            forest.extend(deep_forest)
    time += 1
    u.finish_time = time
    u.color = "black"
    return time, forest


def strongly_connected_components(graph: Graph) -> list[list[str]]:
    dfs(graph)
    print(graph, end="\n\n")
    graph_transpose = graph.transpose()
    forest = dfs_forest(graph_transpose, "by finish time")
    print(graph_transpose, end="\n\n")
    return forest.values()


def topological_sort(graph: Graph) -> list[str]:
    for u in graph.vertices():
        u.color = "white"
        u.parent = "nil"
    time = 0
    topological_sorted_list = []
    for u in graph.vertices("alphabetically"):
        if u.color == "white":
            time = topological_sort_visit(graph, u, time, topological_sorted_list)
    return topological_sorted_list


def topological_sort_visit(
    graph: Graph,
    u: Vertex,
    time: int,
    linked_list: list,
) -> int:
    time += 1
    u.discovery_time = time
    u.color = "gray"
    for v in graph.adjacents(u):
        if v.color == "white":
            v.parent = u.name
            time = topological_sort_visit(graph, v, time, linked_list)
    time += 1
    u.finish_time = time
    u.color = "black"
    linked_list.insert(0, u.name)
    return time


def main() -> None:
    graph = Graph(name="Original")
    graph["a"] = Vertex(name="a", adjacents=["c"])
    graph["b"] = Vertex(name="b", adjacents=[])
    graph["c"] = Vertex(name="c", adjacents=["a"])
    graph["d"] = Vertex(name="d", adjacents=["a", "f"])
    graph["e"] = Vertex(name="e", adjacents=["g"])
    graph["f"] = Vertex(name="f", adjacents=["b", "h"])
    graph["g"] = Vertex(name="g", adjacents=["c", "e", "f", "h"])
    graph["h"] = Vertex(name="h", adjacents=["d"])

    sccs = strongly_connected_components(graph)
    for i, component in enumerate(sccs, 1):
        print(f"SCC {i}: {component}")

    graph = Graph(name="Original")
    graph["a"] = Vertex(name="a", adjacents=["b", "c", "d", "e"])
    graph["b"] = Vertex(name="b", adjacents=["c", "f"])
    graph["c"] = Vertex(name="c", adjacents=["f", "g"])
    graph["d"] = Vertex(name="d", adjacents=[])
    graph["e"] = Vertex(name="e", adjacents=[])
    graph["f"] = Vertex(name="f", adjacents=["g", "h"])
    graph["g"] = Vertex(name="g", adjacents=[])
    graph["h"] = Vertex(name="h", adjacents=[])
    print()
    print("-Topological sort of graph-")
    print(topological_sort(graph))


if __name__ == "__main__":
    main()
