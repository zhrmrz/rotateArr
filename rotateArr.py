class Sol:
    def rotateArr(self,arr,k):
        arr[0:len(arr)-k],arr[len(arr)-k:]=arr[len(arr)-k:],arr[0:len(arr)-k]
        return arr
if __name__ == '__main__':
    p1=Sol()
    print(p1.rotateArr([1,2,3,4,5,6],5))
