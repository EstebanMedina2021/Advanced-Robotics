from shoots import max_arrows

if __name__ == "__main__":
    N, K = map(int, input().split())
    arrows = list(map(int, input().split()))
    result = max_arrows(N, K, arrows)
    print(result)
