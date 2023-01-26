class BTNode {
    constructor(value) {
        this.val = value;
        this.left = null;
        this.right = null;
    }
}
class BST {
    constructor() {
    this.root = null;
    }
    addNode(val) {
    var new_node = new BTNode(val);
    if (this.root === null) {
        this.root = new_node;
        return this;
    }
    let runner = this.root;
    while (runner !== null) {
        if (val > runner.val) {
            if (runner.right == null) {
                runner.right = new_node;
                return this;
            }
            runner = runner.right;
        }
        else if (val < runner.val) {
            if (runner.left == null) {
                runner.left = new_node;
                return this;
            }
            runner = runner.left;
        }
        else if (val == runner.val) {
            runner.left = new_node;
            return this;
        }
    }
}
    contains(val) {
        if (this.root == null) {
            return false;
        }
        let runner = this.root;
        while (runner != null) {
            if (runner.val == val) {
                return true;
            }
            if (val > runner.val) {
                runner = runner.right;
            }
            else {
                runner = runner.left;
            }
        }
        return false;
    }
    findMin(val) {
        if (this.root == null) {
            return "Empty Tree"
        }
        let runner = this.root;
        while (runner.left != null) {
            runner = runner.left;
        }
        return runner.val;
    }
    findMax(val) {
        if (this.root == null) {
            return "Empty Tree"
        }
        let runner = this.root;
        while (runner.right != null) {
            runner = runner.right;
        }
        return runner.val;
    }
    isEmpty() {
        if (this.root == null) {
            return "Empty Tree";
        }
    }
    branchSums() {
        let root = this.root
        let sums = []
        this.calBranchSums(root, 0, sums)
        return sums
    }
    calBranchSums(node, runningSums, sums) { 
        if (node == null) {
            return
        }
        let newRunningSum = runningSums + node.val;
        if (!node.left && !node.right) {
            sums.push(newRunningSum)
            return
        } 
        this.calBranchSums(node.left, newRunningSum, sums)
        this.calBranchSums(node.right, newRunningSum, sums)
    }
    
    
}

let myTree = new BST();

myTree.root = new BTNode(8);


myTree.addNode(10)
myTree.addNode(3)
myTree.addNode(1)
myTree.addNode(6)
myTree.addNode(14)
myTree.addNode(4)
myTree.addNode(7)
myTree.addNode(13)

console.log(myTree.branchSums())



