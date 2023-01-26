function findClosestValueInBst(tree, target) {
    let newtree = tree;
    let distance = Infinity;
    let closest = tree.root;
    while (newtree.value !== null) {
        if (newtree.value == target) {
            return newtree.value;
        }
        if (newtree.value > target) {
            let current = newtree.value - target;
            if (current < distance) {
              distance = current;
              closest = newtree.value;
            }
            if (newtree.left == null){
                return closest;
            }
            else{
                newtree = newtree.left;
            }
        }
        else {
            let current = target - newtree.value;
            if (current < distance) {
              distance = current;
              closest = newtree.value;
            }
            if (newtree.right == null){
                return closest;
            }
            else {
                newtree = newtree.right; 
            }
    }
}
}

class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}