// types.ts
export interface TerraformState {
  version: string;
  terraform_version: string;
  serial: number;
  lineage: string;
  deployments: Deployment[];
}

export interface Deployment {
  id: string;
  serial: number;
  created_at: string;
  checkpoint.blocks: Block[];
}

export interface Block {
  id: string;
  type: string;
  attributes: { [key: string]: string };
  depends_on: string[];
  meta: { [key: string]: string };
}

export type Resource = {
  id: string;
  type: string;
  provider: string;
  depends_on: string[];
  primary: {
    id: string;
    attributes: { [key: string]: string };
    meta: { [key: string]: string };
  };
  deposed: {
    id: string;
    attributes: { [key: string]: string };
    meta: { [key: string]: string };
  }[];
};

export interface InfraTerraformConfig {
  aws_region: string;
  aws_access_key_id: string;
  aws_secret_access_key: string;
  terraform_state_file: string;
  terraform_working_dir: string;
}

export type InfraTerraformResources = {
  [key: string]: Resource;
};